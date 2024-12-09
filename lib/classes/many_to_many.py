class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # List of articles by this author
        print(f"Author '{self.name}' created.")  # Debugging print

    @property
    def name(self):
        return self._name  # Read-only property, no setter

    def articles(self):
        # Ensure the articles are of type Article
        articles = [article for article in Article.all_articles if article.author == self]
        return articles

    def magazines(self):
        # Ensure uniqueness by using set, then return as list
        magazines = {article.magazine for article in self.articles()}
        return list(magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        article = Article(self, magazine, title)
        self._articles.append(article)  # Add article to author's list
        return article  # Return the newly created article

    def topic_areas(self):
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories) if categories else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)
        print(f"Magazine '{self.name}' created with category '{self.category}'.")  # Debugging print

    @property
    def name(self):
        return self._name  # Read-only property, no setter

    @property
    def category(self):
        return self._category  # Read-only property, no setter

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        magazine_article_counts = {mag: 0 for mag in cls.all_magazines}
        for article in Article.all_articles:
            magazine_article_counts[article.magazine] += 1
        return max(magazine_article_counts, key=magazine_article_counts.get, default=None)


class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
        print(f"Article '{self.title}' by {self.author.name} in magazine '{self.magazine.name}' created.")  # Debugging print

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title
