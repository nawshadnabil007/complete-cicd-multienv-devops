from flask import Flask, jsonify
   import os
   from datetime import datetime

   app = Flask(__name__)

   PORT = int(os.getenv('PORT', 3000))
   ENV = os.getenv('ENVIRONMENT', 'development')
   VERSION = os.getenv('VERSION', '1.0.0')

   @app.route('/health')
   def health():
       return jsonify({
           'status': 'healthy',
           'environment': ENV,
           'version': VERSION,
           'timestamp': datetime.utcnow().isoformat()
       })

   @app.route('/')
   def home():
       return jsonify({
           'message': 'DevOps CI/CD Application',
           'environment': ENV,
           'version': VERSION
       })

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=PORT)