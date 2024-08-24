class Config:
    is_production_mode: False
    is_cron_only: False

    def set_runtime_config(self, is_production_mode=False, is_cron_only=False):
        self.is_production_mode = is_production_mode
        self.is_cron_only = is_cron_only


# globally available config
config = Config()
