from app import create_app, db
from app.models import Usuario

app = create_app()
with app.app_context():
    # Crear admin si no existe
    admin = Usuario.query.filter_by(username='admin').first()
    if not admin:
        admin = Usuario(username='admin', rol='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario admin creado: admin / admin123")
    else:
        print("✅ Usuario admin ya existe")

    print("Usuarios en BD:", Usuario.query.count())
