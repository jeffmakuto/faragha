from django.test import TestCase
from ilm.models.user_progress import UserProgress
from ilm.models.quiz import Quiz
from ilm.models.quiz import Question

class UserProgressModelTest(TestCase):
  """
  Test case for the user progress model class
  """
  def setUp(self):
    """
    Creates sample data for testing
    """
    self.quiz = Quiz.objects.create(title='Test Quiz')
    self.question = Question.objects.create(
      quiz = self.quiz,
      text='Test question text',
      corect_answer='Option A',
      options=['Option A', 'Option B', 'Option C']
    )
    user_progress = UserProgress.objects.create(
      user_id = 1,
      quiz = self.quiz,
      question = self.question,
      is_completed = True,
      score = 10
    )

  def test_user_progress_creation(self):
    """
    Verifies user progress can be created
    """
    self.assertEqual(user_progress.user_id, 1)
    self.assertEqual(user_progress.quiz, self.quiz)
    self.assertEqual(user_progress.question, self.question)
    self.assertTrue(user_progress.is_completed)
    self.assertEqual(user_progress.score, 10)