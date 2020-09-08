from models import PurchaseOrder
from djblets.datagrid.grids import Column, DataGrid

class BookDataGrid(DataGrid):
    name = Column("Name", sortable=True, link=True)
    publisher = Column("Publisher", sortable=True, link=True)
    publication_date = Column("Publication Date", sortable=True)

    def __init__(self, request):
            DataGrid.__init__(self, request, queryset=PurchaseOrder.objects.all(), title="Book")
            self.default_sort = ['name']
            self.default_columns = ['name', 'publisher', 'publication_date']