### start project
```
# 以开发模式运行
$ export FLASK\_ENV=development

# 指定入口文件
$ export FLASK\_APP=manage.py

$ flask run
```

### open url: http://127.0.0.1:5000/api/v1.0/
```
http://127.0.0.1:5000/api/v1.0/

```

### create table
```sql
CREATE TABLE `base_user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `username` varchar(60) NOT NULL DEFAULT '' COMMENT '用户名',
  `password_hash` varchar(128) NOT NULL DEFAULT '' COMMENT '密码',
  `mobile` varchar(11) NOT NULL DEFAULT '' COMMENT '手机',
  `avatar_url` varchar(255) NOT NULL DEFAULT '' COMMENT '头像',
  `create_time` datetime COMMENT '创建时间',
  `update_time` datetime COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `learn_plan` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `content` varchar(255) NOT NULL DEFAULT '' COMMENT '内容',
  `author_id` bigint unsigned NOT NULL COMMENT '用户id',
  `expect_finish_time` datetime DEFAULT NULL COMMENT '期望完成时间',
  `actual_finish_time` datetime DEFAULT NULL COMMENT '实际完成时间',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `is_delete` int NOT NULL DEFAULT '0' COMMENT '是否删除，0否，1是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```


### pack this project depend on the package
```
这个操作会将当前已安装的所有 Python 包（也就是项目依赖）的名称及版本号写入文件
requirements.txt 中
$ pip freeze > requirements.txt

然后使用下面命令进行依赖的安装
$ pip install -r requirements.txt

```

### query api
``` python
# 查询id为1的记录
UserModel.query.filter_by(id=1).all()
# 查询id为1的记录只取一条
UserModel.query.filter_by(id=1).limit(1).all()
# 查询符合条件的记录根据id排序只取2条
UserModel.query.order_by(UserModel.id).limit(2).all()
UserModel.query.order_by(UserModel.id.desc()).limit(2).all()
UserModel.query.filter(UserModel.username.endswith('维奇')).order_by(UserModel.id.desc()).limit(2).all()
UserModel.query.filter(UserModel.username.startswith('阿尔')).order_by(UserModel.id).limit(2).all()
UserModel.query.filter(UserModel.username.contains('尔维')).order_by(UserModel.id).all()
# 查询符合限制条的第一条
UserModel.query.filter_by(id=2).first()
UserModel.query.filter_by(id=1).first_or_404()
# 根据主键查询
UserModel.query.get(1)
UserModel.query.get_or_404(1)

```
> 使用 get_or_404() 来代替 get()，使用 first_or_404() 来代替 first(),对于不存在的条目返回一个 404 错误，而不是返回 None。

### 统计符合条件的数量
```
UserModel.query.filter_by(id=1).count()
```

### group分组统计
```
SELECT base_user.username AS base_user_username, count(base_user.mobile) AS count_1 
FROM base_user GROUP BY base_user.username
```
> 用 flask_sqlachemy 表示，返回的是一个 list
```
from sqlalchemy import func
UserModel.query.with_entities(UserModel.username, func.count(UserModel.mobile)).group_by('username').all()
```

### 原生查询
```
from sqlalchemy import text
UserModel.query.filter(text('id>=:value1 and id <:value2')).params(value1=2,value2=5).all()
UserModel.query.from_statement(text("select * from base_user where id=:value")).params(value=1).all()

db.session.execute("SELECT COUNT(*) FROM table").scalar()  # 返回的数字
```

### 分页
```
UserModel.query.paginate(page, per_page,Error_out)
1.  page: 哪一个页
2.  per_page: 每页多少条数据
3.  Error_out: False 查不到不报错
4.  pages: 共有多少页
5.  items: 当前页数的所有对象
user_obj = UserModel.query.paginate(2,2,False)
user_obj.page
user_obj.per_page
user_obj.pages
```

### 查询条件
#### and 
```
from sqlalchemy import and_
UserModel.query.filter(and_(UserModel.username == '阿尔维奇',UserModel.id==1)).all()

或者
UserModel.query.filter(UserModel.username == '阿尔维奇',UserModel.id == 1).all()
```

#### or
```
from sqlalchemy import or_
UserModel.query.filter(or_(UserModel.username == '阿尔维奇', UserModel.username == 'Python')).all()
```

#### in
```
UserModel.query.filter(UserModel.id.in_([1,2])).all()
```

#### not in
```
UserModel.query.filter(~UserModel.id.in_([1,2])).all()
```

#### like
```
UserModel.query.filter(UserModel.username.like('阿尔%')).all()
```

### [Jinja template](http://docs.jinkan.org/docs/jinja2/templates.html#template-inheritance)
```

http://docs.jinkan.org/docs/jinja2/templates.html#template-inheritance
```

### cache
```
Flask 本身不提供缓存，但是 Flask-Caching 扩展可以。 Flask-Caching 支持多种后端，甚至可以支持你自己开发的后端。

内置常用缓存类型

null: 不缓存 (default)
simple: 简单缓存
filesystem: 文件系统缓存
redis: Redis缓存 (redis required)
redissentinel: RedisSentinelCache -> Redis哨兵模式缓存 (redis required)
rediscluster: RedisClusterCache -> Redis集群模式缓存(redis required)
uwsgi: UWSGI缓存 (uwsgi required)
memcached: Memcached缓存 (pylibmc or memcache required)
gaememcached: same as memcached (for backwards compatibility)
saslmemcached: SASLMemcachedCache (pylibmc required)
spreadsaslmemcached: SpreadSASLMemcachedCache (pylibmc required)
```

# 队列
```
 celery -A app.tasks worker -l info
```
