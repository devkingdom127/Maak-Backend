from flask_restx import Resource, fields

model = api.model('Model', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
})

@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return db_get_todo()  # Some function that queries the db