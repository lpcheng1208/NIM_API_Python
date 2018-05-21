# -*- coding: utf-8 -*-

FRIEND_ADD_SILENTLY = 1  # 直接加好友
FRIEND_ADD_REQUEST = 2  # 请求加好友
FRIEND_ADD_AGREE = 3  # 同意加好友
FRIEND_ADD_REFUSE = 4  # 拒绝加好友


RELATION_TYPE_BLACK = 1  # 黑名单操作
RELATION_TYPE_MUTE = 2  # 静音列表操作

OP_VALUE_REMOVE = 0  # 取消黑名单或静音
OP_VALUE_ADD = 1  # 加入黑名单或静音

MESSAGE_OPE_USER = 0  # 点对点个人消息
MESSAGE_OPE_TEAM = 1  # 群消息

MESSAGE_TYPE_TEXT = 0  # 文本消息
MESSAGE_TYPE_IMAGE = 1  # 图片消息
MESSAGE_TYPE_AUDIO = 2  # 语音消息
MESSAGE_TYPE_VIDEO = 3  # 视频消息
MESSAGE_TYPE_LOCATION = 4  # 地理位置消息
MESSAGE_TYPE_FILE = 6  # 文件消息
MESSAGE_TYPE_CUSTOM = 100  # 自定义消息类型

ATTACH_MESSAGE_TYPE_USER = 0  # 点对点自定义系统通知
ATTACH_MESSAGE_TYPE_TEAM = 1  # 群消息自定义系统通知

RECALL_TYPE_USER = 7  # 点对点消息撤回
RECALL_TYPE_TEAM = 8  # 表示群消息撤回

TEAM_CREATE_SILENTLY = 0  # 不需要被邀请人同意
TEAM_CREATE_AGREE = 1  # 需要被邀请人同意

TEAM_JOIN_MODE_OPEN = 0  # 不用验证
TEAM_JOIN_MODE_CHECK = 1  # 需要验证
TEAM_JOIN_MODE_CLOSE = 2  # 不允许任何人加入

TEAM_QUERY_MESSAGE_ONLY = 0  # 0表示不带群成员列表
TEAM_QUERY_MESSAGE_MEMBERS = 1  # 1表示带上群成员列表

TEAM_CHANGE_OWNER_LEAVE = 1  # 群主解除群主后离开群
TEAM_CHANGE_OWNER_NOT_LEAVE = 2  # 群主解除群主后成为普通成员

TEAM_MESSAGE_MUTE = 1  # 关闭消息提醒
TEAM_MESSAGE_UN_MUTE = 2  # 打开消息提醒

TEAM_MEMBER_MUTE = 1  # 禁言
TEAM_MEMBER_UN_MUTE = 0  # 解禁

TEAM_MUTE_TYPE_UN_MUTE = 0  # 解除禁言
TEAM_MUTE_TYPE_MEMBERS_ONLY = 1  # 禁言普通成员
TEAM_MUTE_TYPE_ALL = 3  # 禁言整个群(包括群主)

EVENT_TYPE_SUBSCRIBE = 1  # 事件类型, 订阅指定人员的在线状态事件，固定设置为1

SUBSCRIBE_TTL_30_DAYS = 2592000  # 有效期，单位：秒。取值范围：60～2592000（即60秒到30天）

HISTORY_QUERY_REVERSE_ASE = 1  # 历史消息查询 按时间正序排列
HISTORY_QUERY_REVERSE_DESC = 2  # 按时间降序排列

HISTORY_QUERY_TYPE_ALL = 1  # 所有
HISTORY_QUERY_TYPE_OFFLINE = 2  # 离线
HISTORY_QUERY_TYPE_NO_OFFLINE = 3  # 非离线

CHATROOM_QUEUE_LEVEL_PERM_ALL = 0  # 所有人都有权限变更队列
CHATROOM_QUEUE_LEVEL_PERM_ADMIN = 1  # 只有主播管理员才能操作变更

CHATROOM_OPT_ADMIN = 1  # 设置为管理员
CHATROOM_OPT_MEMBER = 2  # 设置普通等级用户
CHATROOM_OPT_BLACK = -1  # 设为黑名单用户
CHATROOM_OPT_MUTE = -2  # 设为禁言用户

CHATROOM_CLIENT_TYPE_WEB = 1  # web
CHATROOM_CLIENT_TYPE_NON_WEB = 2  # 非web
CHATROOM_CLIENT_TYPE_MP = 3  # 小程序

CHATROOM_MEMBER_TYPE_FIX = 0  # 固定成员
CHATROOM_MEMBER_TYPE_TEMP = 1  # 非固定成员
CHATROOM_MEMBER_TYPE_FIX_ONLINE = 2  # 仅返回在线的固定成员