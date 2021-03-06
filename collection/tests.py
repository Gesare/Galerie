from django.test import TestCase
from .models import Image,Location,Category

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(loc='Nairobi')
        self.location.save()

        self.category = Category(cat='Cars')
        self.category.save()

        self.image_test = Image(description='This is a test instance',image_location=self.location,image_category=self.category)
        self.image_test.save_image()

        self.image_test1 = Image(description='This is a test instance',image_location=self.location,image_category=self.category)
        self.image_test1.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test,Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.image_test.save_image()
        self.image_test.delete_image()
        self.image_test1.delete_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id,'collection/test_one.jpg')
        changed_img = Image.objects.filter(pic='collection/test_one.jpg')
        self.assertTrue(len(changed_img)>0)

    def test_get_image_by_id(self):
        found_img = self.image_test.get_image_by_id(self.image_test.id)
        img = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_img,img)

    def test_search_image_by_category(self):
        category = 'Cars'
        found_img = self.image_test.get_image_by_cat(category)
        self.assertTrue(len(found_img)>1)

    def test_search_image_by_location(self):
        location = 'Nairobi'
        found_img = self.image_test.get_image_by_location(location)
        self.assertTrue(len(found_img)>1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(loc='Nairobi')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_update_location(self):
        new_location_name = 'Paris'
        self.location.update_loc(self.location.id,new_location_name)
        changed_location = Location.objects.filter(loc='Paris')
        self.assertTrue(len(changed_location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)

    def tearDown(self):
        Location.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(cat='Cars')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_update_category(self):
        new_category_name = 'Food'
        self.category.update_cat(self.category.id,new_category_name)
        changed_category = Category.objects.filter(cat='Food')
        self.assertTrue(len(changed_category)>0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)