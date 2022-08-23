from flask import Blueprint, render_template

from app.models import ProductModel

bp = Blueprint('product', __name__, url_prefix='/product')




@bp.route('/list/')
def _list():
    product_list = ProductModel.query.order_by(ProductModel.create_date.desc())
    return render_template('product/product_list.html', product_list=product_list)


@bp.route('/detail/<int:product_id>/')
def detail(product_id):
    product = ProductModel.query.get_or_404(product_id)
    return render_template('product/product_detail.html', product=product) 



# 상품 등록 create


# 상품 수정 update


# 상품 삭제 delete

