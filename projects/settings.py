def add_setting(settings_dict, setting_tuple):
	key = str(setting_tuple[0]).lower()
	value = str(setting_tuple[1]).lower()

	if key in settings_dict:
		return f"Setting '{key}' already exists! Cannot add a new setting with this name."

	settings_dict[key] = value
	return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, setting_tuple):
	key = str(setting_tuple[0]).lower()
	value = str(setting_tuple[1]).lower()
	if key in settings_dict:
		settings_dict[key] = value
		return f"Setting '{key}' updated to '{value}' successfully!"

	return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, setting):

    key = setting.lower()

    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

def view_settings(settings_dict):
	if not settings_dict:
		return f"No settings available."

	return_str = "Current User Settings:\n"
	for key, value in settings_dict.items():
		return_str += (f"{key.capitalize()}: {value}\n")

	return return_str

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
