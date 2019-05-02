from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from blog.models import BlogArticles

class TestAPi(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.data = {
            "title": "Lorem Ipwwr wergwekr ssom Test",
            "content": "<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam<strong> libero dolor nemo dolorem</strong> repudiandae assumenda fugit magnam?&nbsp;Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2019/04/22/security.png\" /></p>\r\n\r\n<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure<em> consequuntur eligendi. Tenetu</em>r perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<h2>snipets</h2>\r\n\r\n<pre>\r\n<code class=\"language-python\">x = 1\r\nif x == 1:\r\n    # indented four spaces\r\n    print(\"x is 1.\")</code></pre>\r\n\r\n<p>&nbsp;</p>",
            "tags": "lorem",
            "publish": True,
            "title_image": "https://media.wired.com/photos/5c1ae77ae91b067f6d57dec0/master/pass/Comparison-City-MAIN-ART.jpg"
        }

        #Create Dummy data
        res1 = BlogArticles.objects.create(
            title = "Lorem Ipsom Test",
            content = "<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam<strong> libero dolor nemo dolorem</strong> repudiandae assumenda fugit magnam?&nbsp;Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2019/04/22/security.png\" /></p>\r\n\r\n<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure<em> consequuntur eligendi. Tenetu</em>r perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<h2>snipets</h2>\r\n\r\n<pre>\r\n<code class=\"language-python\">x = 1\r\nif x == 1:\r\n    # indented four spaces\r\n    print(\"x is 1.\")</code></pre>\r\n\r\n<p>&nbsp;</p>",
            tags = "lorem",
            publish = True,
            title_image = "https://media.wired.com/photos/5c1ae77ae91b067f6d57dec0/master/pass/Comparison-City-MAIN-ART.jpg"
        )
        res2 = BlogArticles.objects.create(
            title = "Ium Test",
            content = "<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam<strong> libero dolor nemo dolorem</strong> repudiandae assumenda fugit magnam?&nbsp;Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2019/04/22/security.png\" /></p>\r\n\r\n<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure<em> consequuntur eligendi. Tenetu</em>r perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<h2>snipets</h2>\r\n\r\n<pre>\r\n<code class=\"language-python\">x = 1\r\nif x == 1:\r\n    # indented four spaces\r\n    print(\"x is 1.\")</code></pre>\r\n\r\n<p>&nbsp;</p>",
            tags = "ium",
            publish = False,
            title_image = "https://www.gettyimages.com/gi-resources/images/500px/983794168.jpg"
        )
        res3 = BlogArticles.objects.create(
            title = "amet consecte",
            content = "<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam<strong> libero dolor nemo dolorem</strong> repudiandae assumenda fugit magnam?&nbsp;Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2019/04/22/security.png\" /></p>\r\n\r\n<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure consequuntur eligendi. Tenetur perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt laudantium itaque iure<em> consequuntur eligendi. Tenetu</em>r perspiciatis enim inventore adipisci, sapiente repellendus quisquam libero dolor nemo dolorem repudiandae assumenda fugit magnam?</p>\r\n\r\n<h2>snipets</h2>\r\n\r\n<pre>\r\n<code class=\"language-python\">x = 1\r\nif x == 1:\r\n    # indented four spaces\r\n    print(\"x is 1.\")</code></pre>\r\n\r\n<p>&nbsp;</p>",
            tags = "omet",
            publish = True,
            title_image = "https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2016/03/1458289957powerful-images3.jpg"
        )

    def test_client_can_get_the_data(self):
        result = self.client.get('/api/')

        self.assertEqual(len(result.json()), 2)
        self.assertEqual(result.status_code, 200)

    
    def test_client_will_never_post(self):
        
        result = self.client.post('/api/', data=self.data)
        self.assertEqual(result.status_code, 405)

