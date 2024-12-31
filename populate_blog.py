import os
import django
from faker import Faker
import random

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supershop.settings')
django.setup()

from blog.models import Post, Category
from django.contrib.auth import get_user_model

# Utilisez le modèle utilisateur personnalisé
User = get_user_model()

fake = Faker()


def create_categories(n=5):
    """Créer des catégories fictives"""
    categories = []
    for _ in range(n):
        name = fake.word().capitalize()
        category = Category.objects.create(name=name, slug=fake.slug(name))
        categories.append(category)
    return categories


def create_posts(n=20, categories=None):
    """Créer des articles fictifs"""
    if categories is None:
        categories = Category.objects.all()

    users = User.objects.all()
    if not users.exists():
        print("Pas d'utilisateurs disponibles pour attribuer les articles.")
        return

    for _ in range(n):
        title = fake.sentence(nb_words=6)
        content = fake.text(max_nb_chars=2000)
        category = random.choice(categories)
        author = random.choice(users)

        Post.objects.create(
            title=title,
            slug=fake.slug(title),
            content=content,
            category=category,
            author=author,
            published=random.choice([True, False])
        )


if __name__ == '__main__':
    print("Création des catégories...")
    categories = create_categories()

    print("Création des articles...")
    create_posts(categories=categories)

    print("Les fausses données ont été créées avec succès.")
