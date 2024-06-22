from app import app, db, Code

# Configuración inicial del contexto de la aplicación Flask
app.app_context().push()

# Eliminar todos los registros de la tabla Code
with db.session.begin():
    db.session.query(Code).delete()

# Confirmar los cambios en la base de datos
db.session.commit()
