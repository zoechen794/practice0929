from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return render_template('index.html', current_time=now)

if __name__ == '__main__':
    # debug=True 在開發模式下方便除錯，代碼修改後會自動重新載入
    app.run(debug=True, host='127.0.0.1', port=5000)
