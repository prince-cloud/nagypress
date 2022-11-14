from configuration.models import City, Region
from typing import Any, Dict, List, Union
from ..models import CategoryGroup, Category, Product, ProductCategory, ProductCategoryGroup, Shop, HotDeal
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from django.contrib.staticfiles.finders import find
from django.contrib.auth import get_user_model
import random

User = get_user_model()


def createImage(image_path: str = None) -> SimpleUploadedFile:
    """Create and return a simple uploaded file"""

    if not image_path:
        image_path = find("test_image.jpg", all=False)
        if not image_path:
            raise Exception("Test ImageFile not Found: test_image.jpg")
    from django.db.models.fields.files import ImageFieldFile
    return InMemoryUploadedFile(file=open(image_path, 'rb'))
    return SimpleUploadedFile(
        name="test_image.jpg",
        content=open(image_path, "rb").read(),
        content_type="image/jpeg",
    )


def createCategoryGroup(
    name="Category Group", avatar=None, mdbico_link=None
) -> CategoryGroup:
    "Create and return a category group"

    category_group =  CategoryGroup(
        name=name, avatar=createImage(avatar), mdbico_link=mdbico_link
    )
    category_group.save()
    return category_group

def createCategory(
    name="Category Group", category_group=None
) -> Category:
    "Create and return a category"
    if not category_group:
        category_group = createCategoryGroup()

    category  = Category(
        name=name, category_group=category_group
    )
    category.save()
    return category




def createProductCategoryGroup(name="Product Category Group", avatar:str=None, mdbico_link:str=None) -> ProductCategoryGroup:
    """Create and return a product Category group"""
    product_category_group = ProductCategoryGroup(
        name=name, avatar=createImage(avatar), mdbico_link=mdbico_link
    )
    product_category_group.save()
    return product_category_group

def createProductCategory(
    name="Product Category", product_category_group=None
) -> ProductCategory:
    "Create and return a product category"
    if not product_category_group:
        product_category_group = createProductCategoryGroup()

    product_category = ProductCategory(
        name=name, category_group=product_category_group
    )
    product_category.save()
    return product_category

def createRegion(name:str = "Bono East") -> Region:
    """Create a region object and return it"""
    region =  Region(name=name)
    region.save()
    return region

def createCity(name: str="My City", region: Region=None):
    """Create and return a city object"""
    if not region:
        region = createRegion()
    city = City(name=name, region=region)
    city.save()
    return city

def createUser(username="TestUser", email="testemail@fabamall.com", password:str="testpassword", picture=None, region = None, city=None, address:str=None, phone_number: str=None) -> User:
    if not region:
        region = createRegion()
    if not city:
        city = createCity()
    user_query = User.objects.filter(username=username)
    if user_query.exists():
        return user_query.first()
    user =  User(username=username, email=email, picture=createImage(picture), region=region, city=city, address=address, phone_number=phone_number)
    user.set_password(password)
    user.save()
    return user

def createShop(name="Test Shop", owner: User=None, categories:List[Category]=None, description:str="Description", about:str="About", website="https://fabamall.com", cover_photo:str=None, is_verified=False, is_premium=False)-> Shop:
    """Create a Shop"""
    if owner == None:
        owner = createUser()
    if not categories:
        categories = [createCategory(f"Category {i}") for i in range(random.randint(1,7))]
    shop =  Shop(name=name, owner=owner, description=description, cover_photo=createImage(cover_photo), is_premium=is_premium, is_verified=is_verified, about=about, website=website)
    shop.save()
    shop.categories.set(categories)
    return shop

def createProduct(title:str="Test Product", shop:Shop= None, description:str="Description", category:ProductCategory=None, is_verified=False, price:float=12.2, featured:bool=False, image: str=None, video:str=None, condition:str="New", quantity:int=None) -> Product:
    """Create a product"""
    if not shop:
        shop = createShop()
    if not category:
        category = createProductCategory()
    product =  Product(title=title, shop=shop, category=category, description=description, is_verified=is_verified, price=price, featured=featured, image=createImage(image), video=video, condition=condition, quantity=quantity)
    product.save()
    return product

def createAll() -> Dict[str, Union[Category, CategoryGroup, Product, Shop, User, Region, City]]:
    """Create and return all objects necessary"""

    return {
        "categoryGroup": createCategoryGroup(),
        "Category": createCategory(),
        "ProductCategory": createProductCategory(),
        "ProductCategoryGroup": createProductCategoryGroup(),
        "Shop": createShop(),
        "Product": createProduct(),
        "User": createUser(),
        "Region": createRegion(),
        "City": createCity()
    }