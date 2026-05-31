from sqlalchemy.orm import Session


def apply_updates(obj, data):
    values = data.model_dump(exclude_unset=True)
    for field, value in values.items():
        setattr(obj, field, value)
    return obj


def create_instance(db: Session, model, data):
    obj = model(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def list_all(db: Session, model):
    return db.query(model).all()


def get_by_pk(db: Session, model, pk_name: str, pk_value):
    return db.query(model).filter(getattr(model, pk_name) == pk_value).first()


def update_by_pk(db: Session, model, pk_name: str, pk_value, data):
    obj = get_by_pk(db, model, pk_name, pk_value)
    if not obj:
        return None
    apply_updates(obj, data)
    db.commit()
    db.refresh(obj)
    return obj


def delete_by_pk(db: Session, model, pk_name: str, pk_value):
    obj = get_by_pk(db, model, pk_name, pk_value)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
