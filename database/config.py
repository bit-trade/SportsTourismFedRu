from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FSTR_DB_HOST: str
    FSTR_DB_PORT: int
    FSTR_DB_LOGIN: str
    FSTR_DB_PASS: str

    @property
    def database_url(self):
        return f'postgresql+psycopg://{self.FSTR_DB_LOGIN}:{self.FSTR_DB_PASS}@{self.FSTR_DB_HOST}:{self.FSTR_DB_PORT}/pereval'

    model_config = SettingsConfigDict(env_file='../.env')


settings = Settings()
