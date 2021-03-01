from app import create_app

# 开发模式创建应用
app = create_app("dev")

if __name__ == '__main__':
    app.run()
