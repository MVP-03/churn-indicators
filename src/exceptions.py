class ChurnAnalysisError(Exception):
    pass


class InvalidAccountDataError(ChurnAnalysisError):
    def __init__(self, account_id: str, errors: list):
        self.account_id = account_id
        self.errors     = errors
        super().__init__(f'Invalid data for account {account_id}: {errors}')


class InsufficientDataError(ChurnAnalysisError):
    def __init__(self, min_required: int, found: int):
        super().__init__(f'Need at least {min_required} accounts, found {found}')
