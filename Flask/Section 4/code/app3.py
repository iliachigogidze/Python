from flask import Flask, request 
from flask_restful import Resource, Api
# from flask_jwt import JWT


app = Flask(__name__)
api = Api(app)
# app.secret_key = 'ilia'

# jwt = JWT(app, authenticate, identity)

universities = []

class University(Resource):
    def get(self, name):
        for university in universities:
            if university['name'] == name:
                return university, 200
        return {'university':None}, 404
            
    def post(self, name):
        data = request.get_json()
        new_university = {
            'name':name,
            'faculties': data['faculties']
        }
        universities.append(new_university)
        return new_university, 201

    def delete(self, name):
        for i, uni in enumerate(universities):
            if uni['name'] == name:
                del universities[i]
                return {'message':'Uni deleted'}
        return universities

    # del put(self, name):
    #     data = request.get_json()
    #     for i, uni in enumerate(universities):
    #         if uni['name'] == name:
    #         else:
    #             universities.append()

    # TODO


class Universities(Resource):
    def get(self):
        return universities, 200

class Faculty(Resource):
    def get(self, name):
        for university in universities:
            if university['name'] == name:
                return university['faculties'], 200
        return {'university':None}, 404

    def post(self, name):
        data = request.get_json()
        for university in universities:
            if university['name'] == name:
                new_faculty = {
                    'faculty_name': data['faculty_name'],
                    'number_of_students': data['number_of_students']
                }
                university['faculties'].append(new_faculty)
                return new_faculty, 201
        return {'university':None}





api.add_resource(University, '/university/<string:name>')
api.add_resource(Universities, '/universities')
api.add_resource(Faculty, '/university/<string:name>/faculties')


app.run(debug=True)

# # [
#     {
#         'faculty_name':'ESM',
#         'number_of_students':120
#     },
#     {
#         'faculty_name':'MACS',
#         'number_of_students':80
#     }
# # ]



# {"faculties":
# 	[
# 		{
# 		    "faculty_name":"ESM",
# 		    "number_of_students":120
# 		},
# 		{
# 		    "faculty_name":"MACS",
# 		    "number_of_students":80
# 		}
# 	]	
# }	