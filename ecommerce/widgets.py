from .views import user_chooser_viewset, attribute_value_chooser_viewset, attribute_chooser_viewset, attribute_group_chooser_viewset

UserChooserWidget = user_chooser_viewset.widget_class
AttributeValueChooserWidget = attribute_value_chooser_viewset.widget_class
AttributeChooserWidget = attribute_chooser_viewset.widget_class
AttributeGroupChooserWidget = attribute_group_chooser_viewset.widget_class