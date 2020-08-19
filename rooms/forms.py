from django import forms

from django_countries.fields import CountryField

from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")

    country = CountryField(default="KR").formfield()

    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )

    price = forms.IntegerField(required=False)

    guests = forms.IntegerField(required=False)

    bedrooms = forms.IntegerField(required=False)

    beds = forms.IntegerField(required=False)

    baths = forms.IntegerField(required=False)

    instant_book = forms.BooleanField(required=False)

    superhost = forms.BooleanField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    menu_1 = forms.CharField(initial="Any food")
    menu_2 = forms.CharField(initial="Any food")
    menu_3 = forms.CharField(initial="Any food")
    menu_4 = forms.CharField(initial="Any food")
    menu_5 = forms.CharField(initial="Any food")


class CreatePhotoForm(forms.ModelForm):
    class Meta:

        model = models.Photo

        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):

        photo = super().save(commit=False)

        room = models.Room.objects.get(pk=pk)

        photo.room = room

        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:

        model = models.Room

        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
            "menu_1",
            "price_1",
            "menu_2",
            "price_2",
            "menu_3",
            "price_3",
            "menu_4",
            "price_4",
            "menu_5",
            "price_5",
        )

    def save(self, *args, **kwargs):

        room = super().save(commit=False)

        return room