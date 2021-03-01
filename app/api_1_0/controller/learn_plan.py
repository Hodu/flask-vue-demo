from flask import render_template
from sqlalchemy import join

from app import db
from app.api_1_0 import bp
from app.api_1_0.model.learn_plan import LearnPlanModel
from app.api_1_0.model.user import UserModel


@bp.route('learn-plan', methods=['GET'])
def learn_plan_index():
    try:
        learn_plan_obj = LearnPlanModel.query.all()
    except Exception as e:
        return '查询失败'

    learn_plans = []
    for learn in learn_plan_obj:
        learn_plans.append(learn.to_dict())
    return render_template("api/learn-plan.html", learns=learn_plans)


@bp.route('learn-plan/<int:_id>', methods=['GET'])
def learn_plan_detail(_id):
    try:
        learn_plan_detail = db.session.query(LearnPlanModel, UserModel)\
            .join(UserModel, LearnPlanModel.author_id == UserModel.id)\
            .filter(LearnPlanModel.id == _id)

    except Exception as e:
        return '查询失败'

    # print("learn_plan_detail ", learn_plan_detail)
    # print("learn_plan_detail ", to_detail(learn_plan_detail))
    learn_plan = []
    for learn in learn_plan_detail:
        print("----->", learn)
        for item in learn:
            if type(item) == LearnPlanModel:
                learn_plan.append(item.to_dict())
            else:
                learn_plan.append(item.to_dict())
    print("result = ", learn_plan)

    return render_template("api/learn-plan-detail.html", learns=learn_plan)
