from django.test import Client, TestCase


from account.models import User
from task_manager.models import Tasks
from task_manager.models.tasks import TaskStatus


from rest_framework import status
from rest_framework.test import APITestCase

from unittest.mock import patch
from unittest.mock import MagicMock


class TestTaskView(TestCase):
    def setUp(self):
        self.client = Client()
        test_user_email = "test@test.com"
        test_password = "1234"
        self.user = User.objects._create_user(
            email=test_user_email,
            password=test_password
        )
        self.client.force_login(self.user)

    def test_task_list(self):

        path = "/tasks/"
        test_task_name ="test task"
        test_default_status = TaskStatus.CREATED
        test_priority = 1

        Tasks.objects.create(
            name=test_task_name,
            priority=test_priority,
            assignee=self.user
        )

        response = self.client.get(path=path)

        self.assertEqual(response.status_code,200)

        objects = response.context["object_list"]
        self.assertEqual(len(objects),1)

        self.assertEqual(objects[0].name , test_task_name)
        self.assertEqual(objects[0].priority, test_priority)
        self.assertEqual(objects[0].status, test_default_status)
        self.assertEqual(objects[0].assignee, self.user)

    def test_create_task(self):
        path = "/tasks/create"

        test_task_name ="test task"
        test_priority = 2
        test_description = "test description"

        body = {
            "name": test_task_name,
            "priority": test_priority,
            "description": test_description
        }

        response = self.client.post(
            path=path,
            data=body
        )
        self.assertEqual(response.status_code,302)

        tasks = Tasks.objects.all()


        self.assertEqual(len(tasks),1)
        self.assertEqual(tasks[0].name,test_task_name)
        self.assertEqual(tasks[0].priority, test_priority)
        self.assertEqual(tasks[0].description, test_description)


    @patch('task_manager.views.user_test_validate')
    def test_mock_view(self,user_test_validate):

        user_test_validate = MagicMock(return_value=True)
        path = "/tasks/users/1"
        response = self.client.get(path=path)
        print(user_test_validate.return_value)


class TestTaskApiView(APITestCase):
    def setUp(self):
        self.client = Client()
        test_user_email = "test@test.com"
        test_password = "1234"
        self.user = User.objects._create_user(
            email=test_user_email,
            password=test_password
        )
        self.client.force_login(self.user)
        self.test_task_name ="test task"
        self.test_priority = 1

        Tasks.objects.create(
            name=self.test_task_name,
            priority=self.test_priority,
            assignee=self.user
        )

    def test_create_api_task(self):

        path = "/tasks/api/tasks/"

        response = self.client.get(path)

        task = response.json()["results"][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task["name"],self.test_task_name)
        self.assertEqual(task["priority"], self.test_priority)
        self.assertEqual(task["assignee"], self.user.id)

        # self.assertEqual(objects[0].name , test_task_name)
        # self.assertEqual(objects[0].priority, test_priority)
        # self.assertEqual(objects[0].status, test_default_status)
        # self.assertEqual(objects[0].assignee, self.user)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')


