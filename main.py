from ariadne import load_schema_from_path, make_executable_schema, \
        graphql_sync, ObjectType, snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api import app, db
from api import models
from api.queries import resolve_words, resolve_word


query = ObjectType("Query")

query.set_field("words", resolve_words)
query.set_field("word", resolve_word)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route('/graphql', methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

