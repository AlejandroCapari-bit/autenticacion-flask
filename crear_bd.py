from app import create_app, db
from app.models import Tarea, Miembro

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Base de datos creada")
    
    # Datos de prueba
    t1 = Tarea(descripcion="Aprender Flask", completado=False)
    t2 = Tarea(descripcion="Usar Bootstrap", completado=False)
    db.session.add_all([t1, t2])
    
    m1 = Miembro(nombre="Ana Pérez", email="ana@example.com")
    m2 = Miembro(nombre="Luis Gómez", email="luis@example.com")
    db.session.add_all([m1, m2])
    
    db.session.commit()
    print("✅ Datos de prueba insertados")
    print(f"Tareas: {Tarea.query.count()}")
    print(f"Miembros: {Miembro.query.count()}")