# Facebook-Page-Post-Image-Text-
Facebook Page Post (Image + Text)

# fp_page_api.py
## How to use this program ?

1. fill your access token details 
2. image file 
3. text you want to put on your page
4. Page ID

```python
if __name__ == '__main__':

    # ENTER YOUR ACCESS TOKEN + PAGE ID 
    access_token = ''                                # ACCESS TOKEN - ENTER YOUR INPUT HERE
    page_id = ''                                     # PAGE ID - ENTER YOUR INPUT HERE
    image_file = 'test.jpeg'                         # IMAGE FILE - ENTER YOUR INPUT HERE
    media_path = os.path.join(os.getcwd(), 'media')

    fb = FbPageAPI(_access_token=access_token)

    fb.create_new_page_directories(image_file)

    fb.post_in_page(fb.get_page_access_token(page_id), page_id, message='GOOD MORNING <3 <3')  # MESSAGE TEXT - ENTER YOUR INPUT HERE

```
