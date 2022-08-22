from readline import append_history_file
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, create_refresh_token,
# )

# import config

app = Flask(__name__)
#api = Api(app)

# # 서명에 사용되는 Key.
# app.config['JWT_SECRET_KEY'] = config.key
# # Access 토큰 만료 기한 (default = 15m)
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = config.access
# # Refresh 토큰 만료 시간 (default = 30m)
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = config.refresh

# jwt = JWTManager(app)


# # Provide a method to create access tokens. The create_access_token()
# # function is used to actually generate the token, and you can return
# # it to the caller however you choose.
# @app.route('/auth', methods=['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     username = request.json.get('username')
#     password = request.json.get('password')

#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400

#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400

#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401

#     # Identity can be any data that is json serializable
#     access_token = create_access_token(identity=username)
#     refresh_token = create_refresh_token(identity=username)

#     return jsonify(access_token=access_token, refresh_token=refresh_token), 200


# # Protect a view with jwt_required, which requires a valid access token
# # in the request to access.
# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200


# @app.route('/refresh', methods=['GET'])
# def refresh():
#     current_user = get_jwt_identity()
#     access_token = create_access_token(identity=current_user)
#     return jsonify(access_token=access_token, current_user=current_user)

# # class Student(Resource):

# #     def get(self, name):
# #         return {'student': name}


# # api.add_resource(Student, '/student/<string:name>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)