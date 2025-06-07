"""Test basic functionality of pydddi package."""

import pytest
from pydddi import IEntity, IModel, IUseCase, ICrudRepository


def test_imports():
    """Test that all main interfaces can be imported."""
    assert IEntity is not None
    assert IModel is not None
    assert IUseCase is not None
    assert ICrudRepository is not None


def test_entity_creation():
    """Test that IEntity can be inherited."""
    from typing import Union

    class TestEntity(IEntity[Union[str, int]]):
        id: Union[str, int]
        name: str

        def get_id(self) -> Union[str, int]:
            return self.id

    # Create instance
    entity = TestEntity(id=1, name="Test")
    assert entity.get_id() == 1
    assert entity.name == "Test"


def test_model_creation():
    """Test that IModel can be inherited."""

    class TestModel(IModel):
        value: str
        number: int

    # Create instance
    model = TestModel(value="test", number=42)
    assert model.value == "test"
    assert model.number == 42


def test_entity_equality():
    """Test entity equality based on ID."""
    from typing import Union

    class TestEntity(IEntity[Union[str, int]]):
        id: Union[str, int]
        name: str

        def get_id(self) -> Union[str, int]:
            return self.id

    entity1 = TestEntity(id=1, name="Test1")
    entity2 = TestEntity(id=1, name="Test2")  # Same ID, different name
    entity3 = TestEntity(id=2, name="Test1")  # Different ID

    assert entity1 == entity2  # Same ID
    assert entity1 != entity3  # Different ID
    assert hash(entity1) == hash(entity2)  # Same hash for same ID
