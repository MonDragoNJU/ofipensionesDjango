class DatabaseRouter:
    """
    Enruta los modelos a las bases de datos correspondientes.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'facturas':
            return 'facturas'
        elif model._meta.app_label == 'reportes':
            return 'reportes'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'facturas':
            return 'facturas'
        elif model._meta.app_label == 'reportes':
            return 'reportes'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'facturas', 'reportes', 'default'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'facturas':
            return db == 'facturas'
        elif app_label == 'reportes':
            return db == 'reportes'
        return db == 'default'
