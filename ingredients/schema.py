import graphene
from graphene_django.types import DjangoObjectType
from .models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query():
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    category = graphene.Field(IngredientType, id=graphene.Int(),
                              name= graphene.String())
    ingredient = graphene.Field(CategoryType,id=graphene.Int(),
                                name=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        print("resolve all categories")
        # print(f'Kwargs - {dir(info)}')
        # print(f'Kwargs - {kwargs}')
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_category(selfself,name,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None
