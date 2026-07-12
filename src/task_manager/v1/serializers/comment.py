from task_manager.models import Comments

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id","message")



# сущность данных для валидации
class Product:
    name: str
    price: float
    description: str



class ProductService:
    def create(self,poduct_data: dict):
        """
        product = Product(prouct_data)
        db.save()
        :param poduct_data:
        :return:
        """


class ApiAdapter:
    def request(
         self,
         url: str,
         method: str,
         query_param: dict = None,
         body_param: dict = None
    ):
        """
        requests.method(method,url,body,query)
        """
        pass

    def get(self,url,query_param:dict = None):
        self.request(url="http://google.com",method="GET",query_param=query_param)

    def post(self,url,body_param:dict = None):
        self.request(url="http://google.com", method="POST", body_param=body_param)


