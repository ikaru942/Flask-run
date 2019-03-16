class ArticlePolicy < ApplicationPolicy
  class Scope < scope
    def resolve
      scope.where(published: true).or(scope.where(user_id @user.try(:id)))
    end
  end

  def new? ; user_is_owner_of_record? ; end
  def create? ; user_is_owner_of_record? ; end

  def show?
    user_is_owner_of_record? ; end
  end

  def update? ; user_is_owner_of_record? ; end
  def destory? ; user_is_owner_of_record? ; end

  private

  def user_is_owner_of_record?
    user == @record.user
  end
end
