class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories) if categories else None

class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_counts = {magazine: len(magazine.articles()) for magazine in cls._all_magazines}
        return max(magazine_counts, key=magazine_counts.get, default=None)
class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an Author instance")
        self._author = new_author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = new_magazine
    @property
    def title(self):
        return self._title