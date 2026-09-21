

class Smartphone:
    def __init__(self, storage_capacity=0):
        self.storage_capacity = storage_capacity
        self.battery = 100
        self.battery_saver_mode = False
        self.storage_used = 0

    def use_battery(self, amount=2):
        if self.battery <= 0:
            raise ValueError("Battery empty. Please recharge.")
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

    def charge_battery(self):
        if self.battery_saver_mode:
            self.battery = 80
        else:
            self.battery = 100

    def storage_left(self):
        return self.storage_capacity - self.storage_used

    def __str__(self):
        saver_status = "Enabled" if self.battery_saver_mode else "Disabled"
        return f"BnL Smartphone - Storage: {self.storage_capacity}GB, Battery: {self.battery}%, Battery Saver Mode: {saver_status}"


class PhotosApp:
    def __init__(self, phone):
        self.phone = phone
        self.num_photos = 0

    def take_photo(self):
        self.phone.use_battery() 
        size = 24 / 1024
        if self.phone.storage_left() >= size:
            self.num_photos += 1
            self.phone.storage_used += size
        else:
            raise ValueError("Not enough storage to take a photo.")

    def delete_photo(self):
        self.phone.use_battery()
        if self.num_photos > 0:
            self.num_photos -= 1
            self.phone.storage_used -= 24 / 1024
        else:
            raise ValueError("No photos to delete.")
            
    #calculate_storage_used disappeared here because of using the smartphone class, it calls from there instead            

    def __str__(self):
        return f"Photos App - Photos: {self.num_photos}, Storage Used: {self.phone.storage_used:.2f}GB"


class YourTubeApp:
    def __init__(self, phone):
        self.phone = phone
        self.videos = []

    def save_video(self, video_duration):
        self.phone.use_battery()
        size = video_duration * 2 / 1024
        if self.phone.storage_left() >= size:
            self.videos.append(video_duration)
            self.phone.storage_used += size
        else:
            raise ValueError("Not enough storage to save video.")

    def delete_video(self, videos_index):
        self.phone.use_battery()
        if 0 <= videos_index < len(self.videos):
            size = self.videos[videos_index] * 2 / 1024
            self.phone.storage_used -= size
            if self.phone.storage_used < 0:
                self.phone.storage_used = 0
            del self.videos[videos_index]
        else:
            raise ValueError("Invalid video index.")
            
    #calculate_storage_used disappeared here because of using the smartphone class, it calls from there instead

    def __str__(self):
        formatted_videos = [f"{m:02}:{s:02}" for m, s in (divmod(v, 60) for v in self.videos)]
        return f"YourTube App - Videos: {formatted_videos}, Storage Used: {self.phone.storage_used:.2f}GB"


def test_phone():
    SP = Smartphone(512)
    for i in range(3):
        SP.use_battery(10)
    print(SP)

    SP.battery_saver_mode = True
    SP.charge_battery()
    print(SP)


def test_photos_app():
    SP = Smartphone(512)
    app = PhotosApp(SP)

    for i in range(5):
        app.take_photo()
    print(app)

    for i in range(2):
        app.delete_photo()
    print(app)


def test_yourtube_app():
    SP = Smartphone(512)
    tubeapp = YourTubeApp(SP)
    print(tubeapp)
    
    tubeapp.save_video(520)
    tubeapp.save_video(241)
    print(tubeapp)
    
def test_storage_left():
    SP = Smartphone(512)
    photos = PhotosApp(SP)
    tubeapp = YourTubeApp(SP)

    photos.take_photo()
    photos.take_photo()
    tubeapp.save_video(761)

    print(f"Storage Left: {SP.storage_left():.2f}GB")

#test_phone()
#test_photos_app()
#test_yourtube_app()
#test_storage_left()
    
    
