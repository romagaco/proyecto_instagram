from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="usuario")
    imagen = models.ImageField(upload_to="posts_images/", verbose_name="imagen")
    caption = models.TextField(max_length=500, blank=True, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True, verbose_name="Numero de likes")


    class Meta:
            verbose_name = "Post"
            verbose_name_plural = "Posts"


    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post alñ que pertenece el comentario", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, verbose_name=" usuario ", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name="contenido del comentario ", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=" Fecha de creacion")

    class Meta:
            verbose_name = "Comentario"
            verbose_name_plural = "Comentarios"
            ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"









