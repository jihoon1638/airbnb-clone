from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(
    models.ServiceOptions,
    models.Accessibility,
    models.Highlights,
    models.Offerings,
    models.DiningOptions,
    models.Amenities,
    models.Atmosphere,
    models.Crowd,
    models.Planning,
    models.Payments,
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.restaurants.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


class MenuInline(admin.TabularInline):
    model = models.Menu


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    """ Restaurant Admin Definition """

    inlines = (PhotoInline,)
    inlines = (MenuInline,)
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "city",
                    "address",
                    "price",
                    "service_options",
                    "guests",
                )
            },
        ),
        (
            "More About the Space",
            {
                "fields": (
                    "highlights",
                    "accessibilities",
                    "offerings",
                    "dining_options",
                    "amenities",
                    "atmosphere",
                    "crowd",
                    "planning",
                    "payments",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "city",
        "price",
        "guests",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_highlights",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "service_options",
        "highlights",
        "accessibilities",
        "offerings",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("highlights", "accessibilities", "offerings")

    def count_highlights(self, obj):
        return obj.highlights.count()

    count_highlights.short_description = "Highlights Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):

    """ Menu Admin Definition """

    list_display = ("__str__", "get_Menu")

    def get_Menu(self, obj):
        return mark_sage()
