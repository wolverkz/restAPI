from celery import Celery

app = Celery('newsweb',
             broker='amqp://172.17.0.1',
             include=['newsweb.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()