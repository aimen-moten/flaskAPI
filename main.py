from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video are required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the Video are required", required=True)

videos = {}

def abort_if_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, "Video ID is invalid!")

def abort_if_exists(video_id):
    if video_id in videos:
        abort(409, "Video with this id already exists!")

class Video(Resource):
    def get(self, video_id):
        abort_if_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return "Successfully Created", 201
    
    def delete(self, video_id):
        abort_if_doesnt_exist(video_id)
        del videos[video_id]
        return "Successfully Deleted", 204

api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
        