class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf',
                    'created_at', 'subscribed_today')
                    'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)
    list_filter = ('paid', 'created_at')

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()
