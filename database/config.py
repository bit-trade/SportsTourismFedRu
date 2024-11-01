from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FSTR_DB_HOST: str
    FSTR_DB_PORT: int
    FSTR_DB_LOGIN: str
    FSTR_DB_PASS: str

    @property
    def database_url(self):
        # postgresql+psycopg://login:pass@localhost:5432/db_name
        return f'postgresql+psycopg://{self.FSTR_DB_LOGIN}:{self.FSTR_DB_PASS}@{self.FSTR_DB_HOST}:{self.FSTR_DB_PORT}/public'

    model_config = SettingsConfigDict(env_file='../.env')

settings = Settings()
