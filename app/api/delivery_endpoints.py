from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.connection import get_db
from app.api.schemas.delivery_schemas import DeliveredPiecesCreate, DeliveredPiecesResponse, DeliveredPiecesUpdate
from app.service.delivery_service import DeliveryService
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/deliveries")
async def get_deliveries(db: Session = Depends(get_db)):
    """Obtener una entrega activa por cada id_group"""
    deliveries = DeliveryService.get_deliveries_one_per_group(db)
    return deliveries


@router.post("/deliveries", response_model=DeliveredPiecesResponse)
async def create_delivery(delivery: DeliveredPiecesCreate, db: Session = Depends(get_db)):
    """Crear una nueva entrega"""
    try:
        logger.info(f"Recibiendo entrega: {delivery}")
        new_delivery = DeliveryService.create_delivery(db, delivery)
        return new_delivery
    except Exception as e:
        logger.error(f"Error al crear entrega: {str(e)}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/deliveries/group/{id_group}")
async def get_deliveries_by_group(id_group: str, db: Session = Depends(get_db)):
    """Obtener todas las entregas activas de un grupo"""
    deliveries = DeliveryService.get_deliveries_by_group(db, id_group)
    if not deliveries:
        raise HTTPException(status_code=404, detail="Grupo de entregas no encontrado")
    return deliveries


@router.get("/deliveries/{delivery_id}", response_model=DeliveredPiecesResponse)
async def get_delivery(delivery_id: int, db: Session = Depends(get_db)):
    """Obtener una entrega por ID"""
    delivery = DeliveryService.get_delivery_by_id(db, delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return delivery


@router.put("/deliveries/{delivery_id}", response_model=DeliveredPiecesResponse)
async def update_delivery(delivery_id: int, delivery: DeliveredPiecesUpdate, db: Session = Depends(get_db)):
    """Actualizar una entrega con registro de auditoría"""
    updated_delivery = DeliveryService.update_delivery(db, delivery_id, delivery)
    if not updated_delivery:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return updated_delivery


@router.delete("/deliveries/{delivery_id}")
async def delete_delivery(delivery_id: int, modified_by: str = None, db: Session = Depends(get_db)):
    """Marcar como inactiva todas las entregas con el mismo id_group y fecha de entrega"""
    # Buscar la entrega para obtener id_group y date
    delivery = DeliveryService.get_delivery_by_id(db, delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    id_group = delivery.id_group
    date = delivery.date
    # Marcar todas las entregas con el mismo id_group y fecha como inactivas
    count = DeliveryService.delete_deliveries_by_group_and_date(db, id_group, date, modified_by)
    if count == 0:
        raise HTTPException(status_code=404, detail="No se encontraron entregas para marcar como inactivas")
    return {"message": f"{count} entregas marcadas como inactivas correctamente", "id_group": id_group, "date": str(date)}