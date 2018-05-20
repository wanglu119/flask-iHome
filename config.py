# coding=utf-8

import redis


class Config:
    """基本配置参数"""
    SECRET_KEY = "TQ6uZxn+SLqiLgVimX838/VplIsLbEP5jV7vvZ+Ohqw="

    # flask-sqlalchemy使用参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@192.168.0.106/python23"  # 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 追踪数据库的修改行为，不设置会报警

    # 创建redis实例用到的参数
    REDIS_HOST = "127.0.0.1"
    REDIS_POST = 6379

    # flask-session使用的参数
    SESSION_TYPE = "redis"  # 保存session数据的地方
    SESSION_USE_SIGNER = True  # 为session id进行签名
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_POST)  # redis实例化
    PEEMANENT_SESSION_LIFETIME = 86400  # session数据的有效期秒


class DevelopmentConfig(Config):
    """开发模式的配置参数"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境的配置参数"""
    pass


config = {
    "development": DevelopmentConfig,  # 开发模式
    "production": ProductionConfig  # 生产/线上模式
}