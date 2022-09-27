from dataclasses import field, fields
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Answer, Question, Quiz, Category

class CategoryType(DjangoObjectType):
  class Meta:
    model = Category
    fields = ('id', 'name')

class QuizType(DjangoObjectType):
  class Meta:
    model = Quiz
    fields = ('id', 'title', 'category', 'quiz')

class QuestionType(DjangoObjectType):
  class Meta:
    model = Question
    fields = ('title', 'quiz')

class AnswerType(DjangoObjectType):
  class Meta:
    model = Answer
    fields = ('question', 'answer_text')

class Query(graphene.ObjectType):
  quiz = graphene.String()
  def resolve_quiz():
    return f"This is the first question"

schema = graphene.Schema(query=Query)
