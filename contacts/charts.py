# import pygal
#
# from .models import Contact
#
#
# class ContactChart():
#
#     def __init__(self, **kwargs):
#         self.chart = pygal.Pie(**kwargs)
#         self.chart.title = 'summary of Contacts'
#
#     def get_data(self):
#         '''
#         Query the db for chart data, pack them into a dict and return it.
#         '''
#         data = {}
#         for detail in Contact.objects.all():
#             data[detail.id
#         return data
#
#     def generate(self):
#         # Get chart data
#         chart_data = self.get_data()
#
#         # Add data to chart
#         for key, value in chart_data.items():
#             self.chart.add(key, value)
#
#         # Return the rendered SVG
#         return self.chart.render(is_unicode=True)
