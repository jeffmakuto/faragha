from django.test import TestCase
from ilm.models.answers import Answer
from ilm.models.questions import Question
from django.core.exceptions import ValidationError


class AnswerModelTest(TestCase):
  """
  Test case for the Answer model class.
  """

  def setUp(self):
    """
    Creates a sample question for testing.
    """
    self.question = Question.objects.create(
      text='Test question text',
      correct_answer='Option A',
      options=['Option A', 'Option B', 'Option C']
    )

  def test_answer_creation(self):
    """
    Verifies that an answer can be created.
    """
    answer = Answer.objects.create(
      question=self.question,
      text='Option A',
      is_correct=True
    )

    self.assertEqual(answer.question, self.question)
    self.assertEqual(answer.text, 'Option A')
    self.assertTrue(answer.is_correct)

  def test_invalid_answer_creation_empty_text(self):
    """
    Verifies that an answer cannot be created with empty text.
    """
    with self.assertRaises(ValidationError):
      Answer.objects.create(question=self.question, is_correct=True)

  def test_invalid_answer_creation_incorrect_text(self):
    """
    Verifies that an answer cannot be created with text not
    in options.
    """
    with self.assertRaises(ValidationError):
      Answer.objects.create(
          question=self.question, text='Invalid Option', is_correct=True
      )

  def test_incorrect_answer(self):
    """
    Verifies that an answer can be created with is_correct=False.
    """
    answer = Answer.objects.create(
        question=self.question, text='Option B', is_correct=False
    )

    self.assertEqual(answer.question, self.question)
    self.assertEqual(answer.text, 'Option B')
    self.assertFalse(answer.is_correct)
