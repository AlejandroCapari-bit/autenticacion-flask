from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Tarea, Miembro

bp = Blueprint('main', __name__)

# ==================== PÁGINA PRINCIPAL ====================
@bp.route('/')
def index():
    return render_template('index.html')

# ==================== CRUD TAREAS ====================
@bp.route('/tareas')
def tareas_listar():
    tareas = Tarea.query.all()
    return render_template('tareas/listar.html', tareas=tareas)

@bp.route('/tareas/crear', methods=['GET', 'POST'])
def tareas_crear():
    if request.method == 'POST':
        tarea = Tarea(
            descripcion=request.form['descripcion'],
            completado='completado' in request.form
        )
        db.session.add(tarea)
        db.session.commit()
        flash('Tarea creada exitosamente', 'success')
        return redirect(url_for('main.tareas_listar'))
    return render_template('tareas/crear.html')

@bp.route('/tareas/editar/<int:id>', methods=['GET', 'POST'])
def tareas_editar(id):
    tarea = Tarea.query.get_or_404(id)
    if request.method == 'POST':
        tarea.descripcion = request.form['descripcion']
        tarea.completado = 'completado' in request.form
        db.session.commit()
        flash('Tarea actualizada', 'success')
        return redirect(url_for('main.tareas_listar'))
    return render_template('tareas/editar.html', tarea=tarea)

@bp.route('/tareas/eliminar/<int:id>')
def tareas_eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    flash('Tarea eliminada', 'success')
    return redirect(url_for('main.tareas_listar'))

# ==================== CRUD MIEMBROS ====================
@bp.route('/miembros')
def miembros_listar():
    miembros = Miembro.query.all()
    return render_template('miembros/listar.html', miembros=miembros)

@bp.route('/miembros/crear', methods=['GET', 'POST'])
def miembros_crear():
    if request.method == 'POST':
        miembro = Miembro(
            nombre=request.form['nombre'],
            email=request.form['email']
        )
        db.session.add(miembro)
        db.session.commit()
        flash('Miembro creado exitosamente', 'success')
        return redirect(url_for('main.miembros_listar'))
    return render_template('miembros/crear.html')

@bp.route('/miembros/editar/<int:id>', methods=['GET', 'POST'])
def miembros_editar(id):
    miembro = Miembro.query.get_or_404(id)
    if request.method == 'POST':
        miembro.nombre = request.form['nombre']
        miembro.email = request.form['email']
        db.session.commit()
        flash('Miembro actualizado', 'success')
        return redirect(url_for('main.miembros_listar'))
    return render_template('miembros/editar.html', miembro=miembro)

@bp.route('/miembros/eliminar/<int:id>')
def miembros_eliminar(id):
    miembro = Miembro.query.get_or_404(id)
    db.session.delete(miembro)
    db.session.commit()
    flash('Miembro eliminado', 'success')
    return redirect(url_for('main.miembros_listar'))