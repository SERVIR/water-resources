from tethys_sdk.base import TethysAppBase, url_map_maker


class WaterResource(TethysAppBase):
    """
    Tethys app class for Water Resource.
    """

    name = 'Water Resource'
    index = 'water_resource:home'
    icon = 'water_resource/images/drop.png'
    package = 'water_resource'
    root_url = 'water-resource'
    color = '#2980b9'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='water-resource',
                controller='water_resource.controllers.home'
            ),
        )

        return url_maps