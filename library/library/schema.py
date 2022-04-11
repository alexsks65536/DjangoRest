import graphene
from graphene_django import DjangoObjectType
from todolist.models import Project, Todo
from users.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    all_todo = graphene.List(TodoType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    todo_by_user_name = graphene.List(TodoType, username=graphene.String(required=False))

    def resolve_todo_by_user_name(self, info, username=None):
        todo = Todo.objects.all()

        if username:
            todo = todo.filter(username__username=username)
        return todo


class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        email = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, firstname, lastname, email, id):
        user = User.objects.get(pk=id)
        user.email = email
        user.username = username
        user.firstname = firstname
        user.lastname = lastname
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



