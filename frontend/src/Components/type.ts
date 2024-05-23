export type PetPolicy = "Cats allowed" | "Pets allowed" | "No pets allowed";

type ValuePiece = Date | null;

export type Value = ValuePiece | [ValuePiece, ValuePiece];