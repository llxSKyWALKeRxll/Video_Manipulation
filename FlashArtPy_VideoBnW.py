import pygame
import cv2

class FlashArt:
    def __init__(self, vid_path, font_size=5):
        pygame.init()
        self.video_path = vid_path
        self.capture_video = cv2.VideoCapture(vid_path)
        self.image = self.load_image()
        #self.capture_video = cv2.VideoCapture(vid_path)
        self.width = self.image.shape[0]
        self.height = self.image.shape[1]
        #self.width = 800
        #self.height = 600
        #self.image = cv2.resize(self.image, (0, 0), fx=0.1, fy=0.1)
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.resolution = self.width, self.height
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.ascii_symbols = '01!\/|@#^*+ILVXT%!'
        self.est_ascii_index = 255 // (len(self.ascii_symbols) - 1)
        self.font = pygame.font.SysFont('C:\\Users\\rebor\\Desktop\\Academics 2k21\\Group Project 2k21\\Flash Art\\VideoBnW_FlashArt_ASCII\\FlashArtFonts_VideoBnW\\f2.ttf', font_size, bold=True)
        self.symbol_gap = int(font_size * 0.4)
        self.rendered_ascii_symbols = [self.font.render(char, False, (255, 255, 255)) for char in self.ascii_symbols]

    def load_image(self):
        temp, self.cv_image = self.capture_video.read()
        #self.cv_image = cv2.imread(self.video_path)
        if not temp:
            exit()
        inverted_image = cv2.transpose(self.cv_image) #To rectify the inversion of the image display in pygame window
        img = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
        #bNw_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
        return img

    def draw_ascii_art(self):
        modified_image = cv2.resize(self.cv_image, (580, 430), interpolation=cv2.INTER_AREA)
        cv2.imshow('Original Image ', modified_image)

    def draw_modified_image(self):
        self.image = self.load_image()
        symbol_locations = self.image // self.est_ascii_index
        for i in range(0, self.width, self.symbol_gap):
            for j in range(0, self.height, self.symbol_gap):
                symbol_location = symbol_locations[i, j]
                if symbol_location:
                    self.screen.blit(self.rendered_ascii_symbols[symbol_location], (i, j))

    def draw_image(self):
        #pygame.surfarray.blit_array(self.screen, self.image)
        #cv2.imshow('Flash_Art', self.image)
        self.screen.fill((0, 0, 0))
        self.draw_modified_image()
        self.draw_ascii_art()

    def save_image(self):
        image = pygame.surfarray.array3d(self.screen)
        cv_image = cv2.transpose(image)
        cv2.imwrite('C:\\Users\\rebor\\Desktop\\Academics 2k21\\Group Project 2k21\\Flash Art\\VideoBnW_FlashArt_ASCII\\FlashArtOutput_VideoBnW\\Flash_Art_Image.png', cv_image)

    def execute(self):
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    exit()
                elif x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_SPACE:
                        self.save_image()
            self.draw_image()
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(25)

flash_art = FlashArt('C:\\Users\\rebor\\Desktop\\Academics 2k21\\Group Project 2k21\\Flash Art\\VideoBnW_FlashArt_ASCII\\FlashArt_VideosBnW\\hagler1.mp4')
flash_art.execute()